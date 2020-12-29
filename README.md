## Installation on tutor:

### app installation:

`cd .local/share/tutor/env/build/openedx/requirements   `

`git clone https://github.com/Hoasker/custom-form-field.git `

`echo "-e ./custom-form-field" >>  private.txt `

`pip3 install -e custom-form-field `


### plugin activation:

`tutor plugins printroot  `

`mkdir "$(tutor plugins printroot)" `

`cd "$(tutor plugins printroot)" `

`nano custom_form_plugin.yml ` Then copy all cods from custom_form_plugin.yml and save

`tutor plugins list `

`tutor plugins enable custom_form_plugin `

`tutor config save `

`tutor images build openedx  `

`tutor local quickstart `

### Debug and development:

`tutor local run lms bash `

`./manage.py lms makemigrations custom_form_field`

`./manage.py lms migrate `

To delete and recreate migrations:
(This step is important if you changed models !)

`./manage.py lms migrate custom_form_field zero `

Than

`./manage.py lms makemigrations custom_form_field `

`./manage.py lms migrate`