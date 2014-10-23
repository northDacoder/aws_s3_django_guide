<h1>John's AWS S3 / Django Cheat Sheet</h1>
<section>
<h3 class="text-left">AWS.AMAZON.COM/console</h3>
<ul class="list-group">
<li class="list-group-item list-group-item-teal">In chrome, go to <a href="aws.amazon.com/console/" target="_blank" class="btn btn-sm btn-warning">AWS Console <i class="fa fa-arrow-circle-o-right"></i></a> & navigate to <span class="label label-danger">S3</span> section of your dashboard</li>
<li class="list-group-item list-group-item-teal">Under <strong>Storage & Content Delivery</strong> click <button class="btn btn-sm btn-primary">create bucket</button></li>
<li class="list-group-item list-group-item-teal">Give the bucket a name & select the <strong>Oregon</strong> region</li>
<li class="list-group-item list-group-item-teal">Open the bucket you created</li>
<li class="list-group-item list-group-item-teal">Create new directories for <strong>"admin"</strong>, <strong>"media"</strong>, & <strong>"static"</strong></li>
<li class="list-group-item list-group-item-teal">In the top right corner of the console click on your <button class="btn btn-sm btn-default"><i class="fa fa-user"></i> username</button>, then <button class="btn btn-default">security credentials</button></li>
<li class="list-group-item list-group-item-teal">click <button class="btn btn-sm btn-default">Continue to Security Credentials</button> on prompt screen</li>
<li class="list-group-item list-group-item-teal">On the left nav, click <button class="btn btn-sm btn-default"><i class="fa fa-user"></i> User</button></li>
<li class="list-group-item list-group-item-teal">Click <button class="btn btn-sm btn-default">Create New User</button> (Make sure the Generate an access key for new user is checked)</li>
<li class="list-group-item list-group-item-teal">Click <button class="btn btn-sm btn-default">Show user security credentials</button> & write down your Access Key ID & your Secret Access Key</li>
<li class="list-group-item list-group-item-teal">Click the <button class="btn btn-sm btn-default">Users</button> tab & the username you just created</li>
<li class="list-group-item list-group-item-teal">Scroll down to permissions & click <button class="btn btn-sm btn-primary">Attach User Policy</button> </li>
<li class="list-group-item list-group-item-teal">With the "Select Policy Template" tab selected, scroll all the way down to S3</li>
<li class="list-group-item list-group-item-teal">Select "Amazon S3 Full Access" policy & hit <button class="btn btn-primary">Apply Policy</button> </li>
<li class="list-group-item list-group-item-teal">Navigate back to your S3 dashboard & go into your bucket directory</li>
<li class="list-group-item list-group-item-teal">Select the "Properties" tab on the right side</li>
<li class="list-group-item list-group-item-teal">Click the <button class="btn btn-sm btn-default">Permissions</button></li>
<li class="list-group-item list-group-item-teal">Click <button class="btn btn-sm btn-default">Add more permissions</button></li>
<li class="list-group-item list-group-item-teal">Under Grantee select <button class="btn btn-sm btn-default">authenticated users</button> & select what access users can have on the bucket (List, Upload/Delete, View Permissions, Edit Permissions)</li>
<li class="list-group-item list-group-item-teal">Click <button class="btn btn-sm btn-primary">SAVE</button></li>
</ul>

<h3 class="text-left">Inside your virtual environment</h3>
<ul class="list-group">
<li class="list-group-item list-group-item-teal">pip install <span class="label label-danger label-sm">Pillow</span></li>
<li class="list-group-item list-group-item-teal">pip install <span class="label label-danger label-sm">Django-storages</span></li>
<li class="list-group-item list-group-item-teal">pip install <span class="label label-danger label-sm">Django-boto</span></li>
<li class="list-group-item list-group-item-teal">pip freeze > requirements.txt </li>
</ul>

<h3 class="text-left">settings.py</h3>
<ul class="list-group">
<li class="list-group-item list-group-item-teal"><i class="fa fa-plus"></i> Add <strong><span class="string">'storages',</span></strong> to the bottom of your installed apps <strong>INSTALLED APPS</strong></li>
</ul>

<h3 class="text-left"><span class="label label-danger"><i class="fa fa-plus"></i> create file</span> s3utils.py (same directory as settings.py)</h3>
<ul class="list-group">
<li class="list-group-item list-group-item-teal">from storages.backends.s3boto import S3BotoStorage <br>StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')</li>
</ul>

<h3 class="text-left">local_settings.py</h3>
<ul class="list-group">
<li class="list-group-item list-group-item-teal">AWS_ACCESS_KEY_ID = <span class="string">'YOUR_ACCESS_KEY_ID'</span></li>
<li class="list-group-item list-group-item-teal">AWS_SECRET_ACCESS_KEY = <span class="string">'YOUR_SECRET_ACCESS_KEY'</span></li>
<li class="list-group-item list-group-item-teal">AWS_STORAGE_BUCKET_NAME = <span class="string">'YOUR_BUCKET_NAME'</span></li>
<li class="list-group-item list-group-item-teal">STATICFILES_STORAGE = <span class="string">'<span style="color: lime; font-weight: 800;">YOUR_PROJECT</span>.s3utils.StaticRootS3BotoStorage'</span></li>
<li class="list-group-item list-group-item-teal">DEFAULT_FILE_STORAGE = <span class="string">'storages.backends.s3boto.S3BotoStorage'</span></li>
<li class="list-group-item list-group-item-teal">S3_URL = <span class="string">'//{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)</span></li>
<li class="list-group-item list-group-item-teal">MEDIA_URL = S3_URL + <span class="string">"media/"</span></li>
<li class="list-group-item list-group-item-teal">STATIC_URL = S3_URL + <span class="string">"static/"</span></li>
<li class="list-group-item list-group-item-teal">ADMIN_MEDIA_PREFIX = STATIC_URL + <span class="string">"admin/"</span></li>
</ul>

<h3 class="text-left">Run collectstatic</h3>
<ul class="list-group">
<li class="list-group-item list-group-item-teal">python manage.py collectstatic</li>