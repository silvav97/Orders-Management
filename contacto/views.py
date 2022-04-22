from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage, send_mail


# Create your views here.


def  contacto(request):

    formulario_contacto = FormularioContacto()
    if request.method=="POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            email_var = EmailMessage("Mensaje desde App Django",
            "El usuario con nombre: {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "", ["sesilvavi@gmail.com"], reply_to=[email])
            try:
                email_var.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
                
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
    
    """
    if request.method=="POST":
        formulario_contacto = FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            infForm = formulario_contacto.cleaned_data
            send_mail(infForm['nombre'], infForm['contenido'],
            infForm.get('email',''), ['sesilvavi@gmail.com'], fail_silently=False )
            #return render(request, "gracias.html")
            #return redirect("/contacto/?valido")
            return render(request, "/contacto/?valido")
    else:
        formulario_contacto = FormularioContacto()
    return render(request, "contacto/contacto.html", {"miFormulario":formulario_contacto})
    """

