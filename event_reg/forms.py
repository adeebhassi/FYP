from django import forms
from .models import *
from django.core.validators import FileExtensionValidator

    
from django import forms


class Event_RegForm(forms.ModelForm):
    AREA_CHOICES = (
        ('','-------'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('bio', 'Biology'),
    )

    DESIGNATION_CHOICES = (
        ('','-------'),
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('others', 'Others'),
    )
    
    FAC_DESIGNATION_CHOICES = (
        ('','-------'),
        ('lecturer', 'Lecturer'),
        ('assistant_professor', 'Assistant Professor'),
        ('associate_professor', 'Associate Professor'),
        ('professor', 'Professor'),
    )
    REG_TYPE=(
        ('','-------'),
        ('regular_reg', 'Regular Registration'),
        ('student_reg', 'Student Registration')
    )
    
    REG_PURPOSE_CHOICES = (
        ('attend', 'For only attending'),
        ('abstract', 'For abstract Submission'),
        ('poster', 'For poster submission'),
    )
    ABSTRACT_TYPE=(
        ('','-------'),
        ('oralpresentation', 'Oral presentation'),
        ('posterpresentation', 'Poster presentation')
    )
    ABSTRACT_CATEGORY=(
        ('','-------'),
        ('physics', 'Physics'), 
        ('chemistry', 'Chemistry'),
        ('bio', 'Biology')
    )
    

    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter your Email","class":"form-control"}))
    area = forms.ModelChoiceField(queryset=Area.objects.all())
    registration_type = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}),choices=REG_TYPE)
    designation = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}),choices=DESIGNATION_CHOICES)
    faculty_designation = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}),choices=FAC_DESIGNATION_CHOICES)
    affiliation = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}),max_length=100)
    fee_receipt = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control","accept":".JPG, .JPEG"}),required=False)
    how_here = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}),max_length=100)
    reg_purpose = forms.ChoiceField(choices=REG_PURPOSE_CHOICES, widget=forms.RadioSelect)
    
    abstract_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}),max_length=100, required=False)
    abstract_type = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}),choices=ABSTRACT_TYPE, required=False)
    abstract_category = forms.ModelChoiceField(queryset=SubArea.objects.all())
    abstract_file = forms.FileField(required=False,widget=forms.FileInput(attrs={"class":"form-control"}))
    keywords=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}),max_length=200,required=False)
    
    poster_title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}),max_length=100, required=False)
    
    terms_conditions = forms.BooleanField(required=True)
    reason = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize: none;',"class":"form-control"}),required=False)
    
    class Meta:
        model = Event_Registration
        exclude = ['status']
        validators=[FileExtensionValidator(allowed_extensions=['docx'])]
        
        
    def clean(self):
        clean_data=super().clean()
        name=clean_data.get('name')
        
        if name and len(name)<9:
            self.add_error('name','Name must contain only alphabtics') 
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['abstract_category'].queryset = SubArea.objects.none()

        if 'area' in self.data:
            print("area is")
            try:
                area_id = int(self.data.get('area'))
                print("hello",area_id)
                self.fields['abstract_category'].queryset = SubArea.objects.filter(area_id=area_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            print("no area")
            self.fields['abstract_category'].queryset = self.instance.area.subarea_set.order_by('name')     
        
    
        
        

