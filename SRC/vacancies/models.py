from django.db import models

# Create your models here.

class vacancy (models.Model):
    WORKINGHOURS = (

        ('6h','6h'),
        ('7h','7h'),
        ('8h','8h'),
        ('9h','9h'),
        ('10h','10h'),

        )

    JOBTITLE= (

        ('Software Engineering','Software Engineering'),
        ('Big data engineer','Big data engineer'),
        ('DevOps Engineer','DevOps Engineer'),
        ('Information systems security manager','Information systems security manager'),
        ('Mobile applications developer','Mobile applications developer'),
        ('Database manager','Database manager'),
        ('Data scientist','Data scientist'),
        ('Network/cloud engineer','Network/cloud engineer'),
        
        )

    WORKSSTATUS= (

        ('Remote','Remote'),
        ('On-Site','On-Site'),
        ('Hybrid','Hybrid'),
      
        
        )

        
    NOOFAPPLICANTS = (

        ('1-5','1-5'),
        ('5-10','5-10'),
        ('10-20','10-20'),
        ('20-50','20-50'),
        ('50+','50+'),
        
        )

    EXPERIENCE = (

        ('Intern','Intern'),
        ('6 months','6 months'),
        ('1 Year','1 Year'),
        ('2 Year','2 Year'),
        ('3 Year','3 Year'),
        ('4 Year','4 Year'),
        ('5 Year','5 Year'),
        ('6 Year','6 Year'),
        ('6+','6+'),
        
        )

 



    company_name =  models.CharField(max_length=200,null=True)
    address =  models.CharField(max_length=200,null=True)
    company_type =  models.CharField(max_length=200,null=True)
    job_title =  models.CharField(max_length=200,null=True,choices=JOBTITLE)
    about_company =  models.CharField(max_length=200,null=True)
    Essentional_duties_responsibilities =  models.CharField(max_length=200,null=True)
    educational_requirements =  models.CharField(max_length=200,null=True)
    #works_status =  models.CharField(max_length=200,null=True,choices=WORKSSTATUS)
    #graduate_status =  models.CharField(max_length=200,null=True)
    #working_status =  models.CharField(max_length=200,null=True)
    working_hours =  models.CharField(max_length=200,null=True,choices=WORKINGHOURS)
    no_of_applicants =  models.CharField(max_length=200,null=True,choices=NOOFAPPLICANTS)
    experience =  models.CharField(max_length=200,null=True,choices=EXPERIENCE)
     

    def __str__(self) :
        return self.company_name




# diliya
class Cvdetails(models.Model):

    name = models.CharField(max_length=100, null=True)
    nic = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile_contact = models.CharField(max_length=10, null=True)
    home_contact = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    ol_result = models.CharField(max_length=100, null=True)
    al_stream = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

# class UserProfile(models.Model):

#     class Meta:
#         verbose_name_plural = 'User Profiles'
#         verbose_name = 'User Profile'
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
#     title = models.CharField(max_length=200, blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     skills = models.ManyToManyField(Skill, blank=True)
#     cv = models.FileField(blank=True, null=True, upload_to="cv")

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'

class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"



# sathma
class comregister(models.Model):

 PROVINCE =(
         ('western','western'),
         ('central','central'),
         ('southern','southern'),
         ('UVA','UVA'),
         ('sabaragamuwa','sabaragamuwa'),
         ('north-western','north-western'),
         ('north-central','north-central'),
         ('northern','northern'),
         ('eastern','eastern'),
 )

# user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
 company_name = models.CharField(max_length=200,null=True)
 name = models.CharField(max_length=200,null=True)
 address = models.CharField(max_length=200,null=True)
 address_line2 = models.CharField(max_length=200,null=True)
 city = models.CharField(max_length=200,null=True)
 postal_zip = models.CharField(max_length=200,null=True)
 province = models.CharField(max_length=200,null=True, choices=PROVINCE)
 description=models.CharField(max_length=200,null=True)
 website_url = models.CharField(max_length=200,null=True)
 business_email = models.CharField(max_length=200,null=True)
 business_contactNo = models.CharField(max_length=200,null=True)
 username = models.CharField(max_length=200,null=True)
 password1 = models.CharField(max_length=200,null=True)
 password2 = models.CharField(max_length=200,null=True)
	

 def __str__(self):
      return self.company_name




class profile(models.Model):


 user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
 company_name = models.CharField(max_length=200,null=True)
 address = models.CharField(max_length=200,null=True)
 address_line2 = models.CharField(max_length=200,null=True)
 description=models.CharField(max_length=200,null=True)
 website_url = models.CharField(max_length=200,null=True)
 business_email = models.CharField(max_length=200,null=True)
 business_contactNo = models.CharField(max_length=200,null=True)
 
	
 def __str__(self):
      return str(self.user)




def create_profile(sender, instance, created, **kwargs):
        if created:
                Profile.objects.create(user=instance)
                print('Profile Created!')

post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
        if created == False:
                instance.profile.save()
                print('Profile updated!')

post_save.connect(update_profile, sender=User)



# pasindu
class Student(models.Model):

    UNIVERSITY = (

        ('Sri Lanka Institute of Information Technology (SLIIT)','Sri Lanka Institute of Information Technology (SLIIT)'),
        ('ESOFT Metro Campus','ESOFT Metro Campus'),
        ('Imperial College of Business Studies','Imperial College of Business Studies'),
        ('AIC Campus','AIC Campus'),
        ('Sri Lanka Technological Campus','Sri Lanka Technological Campus'),
        ('NSBM Green University','NSBM Green University'),
        ('ICBT Campus','ICBT Campus'),
        ('NIBM - National Institute of Business Management','NIBM - National Institute of Business Management'),
        ('CINEC Metro Campus','CINEC Metro Campus'),
        ('British Institute of Engineering and Technology, Sri Lanka','British Institute of Engineering and Technology, Sri Lanka'),
        ('IMBS Green Campus','IMBS Green Campus'),
        ('APIIT Sri Lanka','APIIT Sri Lanka'),
        ('Informatics Institute of Technology (IIT)','Informatics Institute of Technology (IIT)'),
        ('KIU','KIU'),
        ('ACBT Campus','ACBT Campus'),
        ('General Sir John Kotelawala Defence University','General Sir John Kotelawala Defence University'),
        ('Horizon Campus','Horizon Campus'),
        ('American College of Higher Education','American College of Higher Education'),
        ('Royal Institute of Colombo','Royal Institute of Colombo'),
    )

    DEGREE = (
        ('BSc (Hons) in Information Technology - Information Technology', 'BSc (Hons) in Information Technology - Information Technology'),
        ('BSc (Hons) in Information Technology - Computer Systems & Network Engineering', 'BSc (Hons) in Information Technology - Computer Systems & Network Engineering'),
        ('BSc (Hons) in Information Technology - Software Engineering','BSc (Hons) in Information Technology - Software Engineering'),
        ('BSc (Hons) in Information Technology - Information Systems Engineering', 'BSc (Hons) in Information Technology - Information Systems Engineering'),
        ('BSc (Hons) in Information Technology - Cyber Security', 'BSc (Hons) in Information Technology - Cyber Security'),
        ('BSc (Hons) in Information Technology - Interactive Media', 'BSc (Hons) in Information Technology - Interactive Media'),
        ('BSc (Hons) in Information Technology - Data Science', 'BSc (Hons) in Information Technology - Data Science'),
        ('Master of Science - in Information Technology', 'Master of Science - in Information Technology'),
        ('Master of Science - in Information Management', 'Master of Science - in Information Management'),
        ('Master of Science - in Information Systems', 'Master of Science - in Information Systems'),
        ('Master of Science - in Information Technology – Cyber Security', 'Master of Science - in Information Technology – Cyber Security'),
        ('Master of Science - in Information Technology – Enterprise Applications Development', 'Master of Science - in Information Technology – Enterprise Applications Development'),
    )

    STATUS = (
        ('Undergraduate - Year 1', 'Undergraduate - Year 1'),
        ('Undergraduate - Year 2', 'Undergraduate - Year 2'),
        ('Undergraduate - Year 3', 'Undergraduate - Year 3'),
        ('Undergraduate - Year 4', 'Undergraduate - Year 4'),
        ('Graduate', 'Graduate'),
        ('Postgraduate', 'Postgraduate'),
        ('Graduate - Masters', 'Graduate - Masters'),
    )


    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact_Number = models.CharField(max_length=200)
    Linkedin_URL = models.CharField(max_length=10000)
    Date_of_Birth = models.DateField(max_length=200)
    university = models.CharField(max_length=5000, null=True, choices=UNIVERSITY)
    degree = models.CharField(max_length=5000, null=True, choices=DEGREE)
    degree_Status = models.CharField(max_length=5000, null=True, choices=STATUS)
    nIC = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    re_enter_password = models.CharField(max_length=200, null=True)
    date_Created = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.name
