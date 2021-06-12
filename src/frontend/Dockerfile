#
# Builder stage.
# This state compiles TypeScript code to build the React app
#

# Build image based on node:14.5 with lerna installed
FROM node:14.5  as builder

LABEL MAINTAINER="SWA"


ENV APP "app"

# when we change our application's nodejs dependencies:
ADD package.json /tmp/package.json
# install dependencies
RUN cd /tmp && npm install


ADD . ${APP}

# Add node_modules to public folder
RUN ln -s /tmp/node_modules /${APP}

# Setting that next commands run on the folder code
WORKDIR /${APP}

# build argument: ie: --build-arg NODE_ENV=prod || NODE_ENV=dev || NODE_ENV=test
ARG NODE_ENV
# This scripts rename .env.local || .env.prod || env.stagging to .env
RUN sh entry_point.sh $NODE_ENV
# Same script but without args, load envVars to build
RUN sh entry_point.sh
# Build the application by defined command in package.json && .env
RUN npm run build

#
# Production stage.
# Final Docker image with Nginx for React app
#

FROM nginx:stable-alpine
ENV APP "app"

# Set nginx configuration for react app
COPY docker/nginx/default.conf /etc/nginx/conf.d/default.conf

# Remove nginx boilerplate assets
RUN rm -rf /usr/share/nginx/html

# Copy application bundles to static nginx->html
COPY --from=builder /${APP}/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
