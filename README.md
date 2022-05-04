# proyecto_final_coderhouse
Proyecto final del curso de Python

"Astrotour" es un sitio web creado como proyecto final del curso de Python de Coderhouse. El sitio web sirve para la adquisicion de tickets a destinos mas alla de la atmosfera terrestre; ademas, cuenta con una comunidad para la interaccion entre usuarios y la posibilidad de enterarse de las noticias mas recientas.

Uno o una puede adoptar diferentes perspectivas del sitio web dependiendo de como este registrado: 
  a) Si ingresa como "usuario no registrado" podra visualizar los destinos y los vehiculos que cuenta la plataforma; pero no podra sacar tickets, ni ingresar al apartado de comunidad.
  b) Si ingresa como "usuario registrado" podra visualizar lo mismo que un "usuario no registrado", agrando la posibilidad de sacar tickets y ver el apartado de comunidad. Ademas, se habilita la opcion de "ver tus tickets", "crear post", "comentar un post", "poner me gusta a un post". Un usuario tiene muchas facultades sobre las acciones que puede realizar en el sitio web. Puede "eliminar sus tickets", "cambiar sus datos de usuario", "eliminar un post suyo", "eliminar un comentario suyo".
  c) Si ingresa como "superusuario" podra administrar, practicamente, todo el sitio web. Se habilita la opcion de "crear un destino" y "crear un vehiculo"; tambien pueden crear entradas en los blogs. Un superusuario puede borrar posts, comentarios, vehiculos, destinos y tickets de los usuarios. Otra pestaña que surge es la de "vuelos", en donde puede visualizar todos los vuelos junto con sus detalles.
  
  urls del sitio web:
  a) /comunidad/
          path('padre_comunidad', views.ver_padre_comunidad),
          path('crear-post', views.crear_post, name = "Crear_posts"),
          path("posts/<id>", views.ver_posteos, name = "Mostrar_posts"),
          path("posteos", views.posteos, name = "Ver_post"),
          path("eliminar-comentario/<pk>", views.Comentario_delate.as_view(), name = "Eliminar_comentario"),
          path("eliminar-post/<pk>", views.Posts_delate.as_view(), name = "Eliminar_posteo"),
          path('likes/<id>', views.dar_like, name="Likes"),
  b) /usuario/
          path('padre', views.padre_template),
          path('login', views.login_request, name = "Login"),
          path('register', views.register, name = 'Register'),
          path('logout', LogoutView.as_view(template_name = 'inicio.html'), name = 'Logout'),
          path('editar', views.editar_perfil, name = 'Editar_perfil'),
          path('register-super', views.register_superusuario, name = 'Register_super'),
          path('perfil', views.perfil_propio, name = 'Perfil_propio'),
          path('perfil-astro/<id>',views.perfil_astroturistas,name="Perfil-astro"),
          path('eliminar-astro/<pk>', views.User_delete.as_view(), name = 'Eliminar-astroturista'),
          path('contactenos', views.contactanos, name = 'Contactenos'),
          path('acerca', views.acerca, name = "Acerca")
  c) /viaje/
          path('padre', views.padre_template),
          path('crear-vehiculo', views.crear_vehiculos, name = "Crear_vehiculo"),
          path('crear-destino', views.crear_destino, name = "Crear_destino"),
          path("mostrar-vehiculos", views.Vehiculos_vista.as_view(), name = "Mostrar_vehiculos"),
          path("mostrar-destinos", views.Destinos_vista.as_view(), name = "Mostrar_destinos"),
          path("mostrar-vuelos", views.Vuelos_vista.as_view(), name = "Mostrar_vuelos"),
          path("mostrar-tickets", views.Tickets_vista.as_view(), name = "Mostrar_tickets"),
          path('crear-ticket', views.crear_ticket, name = "Crear_ticket"),
          path("ticket-usuario", views.mostrar_tickets_astroturista, name = "Mostrar_tickets_usuario"),
          path("eliminar-vehiculo/<pk>", views.Vehiculos_delete.as_view(), name = "Eliminar_vehiculo"),
          path("eliminar-destino/<pk>", views.Destino_delete.as_view(), name = "Eliminar_destino"),
          path("editar-vehiculo/<pk>", views.Vehiculos_update.as_view(), name = "Editar_vehiculo"),
          path("editar-destino/<pk>", views.Destino_update.as_view(), name = "Editar_destino"),
          path("pagos", views.prueba_pagos),
          path("", views.inicio, name = "Inicio"),
          path("tickets-admin", views.ver_tickets_admin, name = "Tickets-admin"),
          path("editar-ticket-admin/<pk>", views.Ticket_admin_delete.as_view(), name = "Eliminar_admin_ticket"),
          path("eliminar-ticket/<pk>", views.Ticket_delete.as_view(), name = "Eliminar_ticket"),
          path("vehiculo/<id>", views.ver_vehiculo, name = "Mostrar_vehiculo"),
          path("destino/<id>", views.ver_destino, name = "Mostrar_destino"),
          path('crear-ticket-tierra', views.volver_tierra, name = "Crear_ticket_tierra"),
