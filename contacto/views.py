from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.http import HttpResponseRedirect

def formulario_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        apellido = request.POST.get('apellido', '')
        email = request.POST.get('email', '')
        telefono = request.POST.get('telefono', '')
        asunto = request.POST.get('asunto', '')
        consulta = request.POST.get('consulta', '')

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

# email = EmailMessage('Test', 'Lorem Ipsum', to=['gobeamariano@gmail.com'])
# email.send()
