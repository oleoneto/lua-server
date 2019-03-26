FROM nginx:1.15.8-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

# Create logs directory
# RUN mkdir /var/www/logs/lualms.com/
# RUN touch /var/www/logs/lualms.com/access.log
# RUN touch /var/www/logs/lualms.com/error.log

CMD ["nginx", "-g", "daemon off;"]
