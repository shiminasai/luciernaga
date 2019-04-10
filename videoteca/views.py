from django.shortcuts import render

# Create your views here

class SendContact(FormView):
    form_class = ContactForm
    template_name = 'contact-us.html'
    success_url = reverse_lazy('<app-name>:contact-us')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(ContactView, self).form_valid(form)

    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data)
        pass

