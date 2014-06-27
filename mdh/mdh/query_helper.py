prefix = """
         PREFIX :<http://hypermedia.demos.techlabs.accenture.com#>
         PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
         PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
         PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
         PREFIX owl:<http://www.w3.org/2002/07/owl#>
         """

products = lambda usr: """SELECT ?transition ?resource
                             ?api_end_point
                             WHERE { :""" + usr + """ ?transition ?resource .
                             ?resource :has_api_end_point ?api_end_point .
                            FILTER (!SAMETERM(?transition,rdf:type))
                             }
                           """

cap = lambda usr: """SELECT ?hypermedia_transition ?resource ?api_end_point
               WHERE { :""" + usr + """ ?p ?o .
               FILTER (!SAMETERM(?p,rdf:type)) .
               ?o ?hypermedia_transition ?resource .
               ?resource :has_api_end_point ?api_end_point .
               }
               """

nwr = lambda usr, nwr_rel: """SELECT ?cap ?transition ?resource
               WHERE { :""" + usr + """ ?p ?o .
               FILTER (!SAMETERM(?p,rdf:type)) .
               ?o ?prop ?cap .
               FILTER (SAMETERM(?cap,:""" + nwr_rel + """)) .
               ?cap ?transition ?resource .
               FILTER (SAMETERM(?transition,:has_network_activation_services)
               ) . }
               """

hyper_graph = {'fruityDeveloper': {'products': products('fruity_developer'),
                                   'capabilities': cap('fruity_developer'),
                                   'network': nwr('fruity_developer',
                                                  'eyeHome_network_capability')
                                   ,
                                   },
               'acnDeveloper': {'products': products('Accenture.User'),
                                'capabilities': cap('Accenture.User'),
                                'network': nwr('Accenture.User',
                                               'network_activation_capability')
                                ,
                                },
               }
