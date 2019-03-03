#These Shell files must be edited on Linux!!!!!!!!!!!!!!!!
#This shell first makes HTML pages for any jpg files found in the NewPhoto-Add directory
#Then moves them to the current Photo year folder, currently 2015 (Defined in Listing-Create)
cd /
python /var/www/Photos/code/NewPhoto-Add/NewPhoto-Add.py
rm /var/www/Photos/code/NewPhoto-Add/Delivery/index.html
chown joabj /var/www/Photos/code/NewPhoto-Add/Delivery/*
mv /var/www/Photos/code/NewPhoto-Add/Delivery/*.jpg /var/www/Photos/2018
mv /var/www/Photos/code/NewPhoto-Add/Delivery/*.html /var/www/Photos/2018
cp /var/www/Photos/code/NewPhoto-Add/index.html /var/www/Photos/code/NewPhoto-Add/Delivery
chown joabj /var/www/Photos/code/NewPhoto-Add/Delivery/*
python /var/www/Photos/code/Listing-Create/Listing-Create.py
