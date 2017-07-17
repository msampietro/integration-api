Integration API for Instapage and Odoo CRM

docker build -t api:flask /root/docker-flask/integration-api/

docker run -d -p 5151:443 -v /root/docker-flask/docker-flask-master/integration-api/docker-volume/:/var/www/integration-api/docker-volume api:flask

docker exec -it [image_id] bash