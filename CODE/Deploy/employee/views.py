from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from employee.forms import EmployeeForm

from django.views.generic import DetailView
from employee.models import Employee


class EmployeeImage(TemplateView):
    form = EmployeeForm
    template_name = 'emp_image.html'

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()

            return HttpResponseRedirect(reverse_lazy('emp_image_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'


def weather(request):
    result1 = Employee.objects.latest('id')
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    import h5py
    models = keras.models.load_model('C:/Users/Deepak Resjad/Desktop/CODE/Deploy/employee/weather5.h5')
    from tensorflow.keras.preprocessing import image
    test_image = image.load_img('C:/Users/Deepak Resjad/Desktop/CODE/Deploy/media/' + str(result1),
                                target_size=(225, 225))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = models.predict(test_image)
    prediction = result[0]
    prediction = list(prediction)
    classes=['cloudy', 'rain', 'shine', 'sunrise']
    output = zip(classes, prediction)
    output = dict(output)
    if output['cloudy'] == 1.0:
        a="cloudy"
    elif output['rain'] == 1.0:
        a="rain"
    elif output['shine'] == 1.0:
        a="shine"
    elif output['sunrise'] == 1.0:
        a="sunrise"

    return render(request, "result.html", {"out": a})
