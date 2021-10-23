from django.shortcuts import render

# Create your views here. Direccionar formulario de contacto

def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar (request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST['txtMensaje'] + " / EMAIL: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["psotocalle@gmail.com"]
        send_mail(asunto, mensaje, email_desde ,email_para, fail_silently=False)
        return render (request, "contactoExitoso.html")
    return render(request, 'formularioContacto.html')

