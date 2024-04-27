from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from contacto.models import Email

def formulario_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        apellido = request.POST.get('apellido', '')
        email = request.POST.get('email', '')
        telefono = request.POST.get('telefono', '')
        asunto = request.POST.get('asunto', '')
        consulta = request.POST.get('consulta', '')

        # Crear un objeto Email y guardarlo en la base de datos
        email_obj = Email.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            asunto=asunto,
            consulta=consulta
        )

        # Constants
        SENDER = 'mariano_gobea@hotmail.com'
        RECEIVER = 'gobeamariano@gmail.com'

        mensaje = f"""
        Nombre: {nombre}
        Apellido: {apellido}
        Email: {email}
        Teléfono: {telefono}
        Asunto: {asunto}
        Consulta: {consulta}
        """

        print(mensaje)

        send_mail(
            asunto,
            mensaje,
            SENDER,
            [RECEIVER],
            fail_silently=False,
        )

        print("Envio el email!!!")

        return JsonResponse({'message': 'Gracias por comunicarte con MGA. A la brevedad nos pondremos en contacto contigo.'})  # Retorna un json para mostrarlo como alert

    return render(request, 'contacto/formulario_contacto.html')  # Renderiza el formulario de contacto si el método de solicitud es GET
