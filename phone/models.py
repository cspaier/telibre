from django.db import models

from wagtail.admin.panels import FieldPanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager
import requests
from bs4 import BeautifulSoup

class ApplicationTag(TaggedItemBase):
    content_object = ParentalKey('phone.Application', on_delete=models.CASCADE, related_name='tagged_items')


class Application(ClusterableModel):
    name = models.CharField(max_length=80, verbose_name="nom")
    url = models.URLField("url", max_length=200, blank=True, null=True)
    tags = TaggableManager(through=ApplicationTag, blank=True, null=True)
    
    
    panels = [
        FieldPanel("name"),
        FieldPanel("url"),
        FieldPanel("tags"),
    ]
    
    def __str__(self):
        return f"{self.name}"



class Phone(models.Model):
    gsmarena_url = models.URLField("gsmarena url", max_length=200)
    brand = models.CharField(max_length=80, verbose_name="marque")
    modelname = models.CharField(max_length=80, verbose_name="modèle")
    year = models.SmallIntegerField(verbose_name="année", blank=True, null=True)
    lineage = models.BooleanField(verbose_name=("Supporte Linéage OS"))
    graphene = models.BooleanField(verbose_name=("Supporte Graphene OS"))
    dimensions = models.CharField(max_length=80, blank=True, null=True, verbose_name="taille")
    cpu = models.CharField(max_length=80, blank=True, null=True, verbose_name="cpu")
    cam1modules = models.CharField(max_length=80, blank=True, null=True)
    cam1video = models.CharField(max_length=80, blank=True, null=True)
    cam2modules = models.CharField(max_length=80, blank=True, null=True)
    weight = models.SmallIntegerField(verbose_name="masse", blank=True, null=True)
    internalmemory = models.CharField(max_length=80, blank=True, null=True)
    nettech = models.CharField(max_length=80, blank=True, null=True)
    usb = models.CharField(max_length=80, blank=True, null=True)
    displaysize = models.CharField(max_length=80, blank=True, null=True)
    img = models.URLField(blank=True, null=True)
    
   
    def __str__(self):
        return f'{self.brand} {self.modele} {self.year}'

    @staticmethod
    def is_gsmarena(url):
        return "www.gsmarena.com" in url

    @staticmethod
    def parse_gsmarena_url(url):
        """Parse a gsmarena url and returns a dictionnary:
        {
            brand:
            model:
            dimensions:
            ...
        }
        """
        data = {}
        if not Phone.is_gsmarena(url):
            return data

        # get gsmarena html
        r = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
        if r.status_code != 200:
            return data
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Brand and model
        brand_modelname = soup.find(attrs={"data-spec": 'modelname'}).contents[0].split(' ')
        brand = brand_modelname[0]
        modelname = " ".join(brand_modelname[1:])
        data.update({
            'brand': brand,
            'modelename': modelname
        })
        
        # img
        model_img_html = soup.find(class_='specs-photo-main')
        data['img'] = model_img_html.find('img')['src']

        # Year
        year = int(soup.find(attrs={"data-spec": 'year'}).contents[0].split(',')[0])
        data['year'] = year
        
        # All other fields doesn't need data parsing
        for field in ['dimensions', 'cpu', 'cam1modules', 'cam1video', 'cam2modules',
                'weight', 'internalmemory', 'nettech', 'usb', 'displaysize']:
            spec = soup.find(attrs={"data-spec": field}).contents[0]
            if spec is None:
                continue
            data[field] =  spec
            
        return data