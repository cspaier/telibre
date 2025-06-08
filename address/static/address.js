// https://gist.github.com/ThomasG77/0b99013795f76699c5c9a0d7daf4411e

var myobject = []
        const postcode = document.querySelector('#id_postcode');
        const city = document.querySelector('#id_city');
        const street = document.querySelector('#id_street');
        const housenumber = document.querySelector('#id_house_number');

        const autoCompleteJS = new autoComplete({
            selector: "#id_autocomplete",
            placeHolder: "Recherche adresse...",
            data: {
                src: async () => {
                   const term = document.querySelector('#id_autocomplete').value;
                   if (term.length > 2) {
                     const response = await fetch(`https://api-adresse.data.gouv.fr/search/?q=${term}`)
                     const json = await response.json()
                     console.log(json)
                     myobject = json.features.map(function(el) {
                        return {
                          label: el.properties.label,
                          value: el.properties.label,
                          housenumber: el.properties.housenumber,
                          name: el.properties.name,
                          postcode: el.properties.postcode,
                          city: el.properties.city,
                          context: el.properties.context,
                          type: el.properties.type,
                          street: el.properties.street,
                          boundingbox: null
                        }
                      })
                      adresses = myobject.map(el => el.value)
                   } else {
                     adresses = []
                   }
                  return adresses
                },
                cache: false,
            },
            resultsList: {
                element: (list, data) => {
                  console.log(data)
                    if (!data.results.length) {
                        // Create "No Results" message element
                        const message = document.createElement("div");
                        // Add class to the created element
                        message.setAttribute("class", "no_result");
                        // Add message text content
                        message.innerHTML = `<span>Found No Results for "${data.query}"</span>`;
                        // Append message element to the results list
                        list.prepend(message);
                    }
                },
                noResults: true,
            },
            resultItem: {
                highlight: true
            },
            events: {
                input: {
                    selection: (event) => {
                        const selection = event.detail.selection.value;
                        autoCompleteJS.input.value = selection;
                        var result = myobject.find(el => el.value == event.detail.selection.value)
                        if (result) {
                          postcode.value = result.postcode;
                          city.value = result.city;
                          street.value = result.street;
                          housenumber.value = result.housenumber;
                        } else {
                          postcode.value = ''
                          city.value = ''
                        }

                    }
                }
            }
        });