const webpack = require('webpack');
const DashboardPlugin = require('webpack-dashboard/plugin');
const argv = require('yargs').argv;

const config = {};
module.exports = config;

config.entry = {
    survey: './src/static/js/app/survey.js',
    generate: './src/static/js/app/generate-survey.js'
};
config.output = {
    path: 'src/static/js',
    filename: '[name].js',
    publicPath: '/static/js/'
};
config.resolve = {
    "alias": {
        "react": "preact-compat",
        "react-dom": "preact-compat"
    }
};
config.module = {
    rules: [
        {
            test: /\.js$/,
            exclude: /node_modules/,
            use: 'babel-loader',
            options: {
                presets: [['es2015', { modules: false }], 'react'],
                plugins: ['transform-class-properties']
            }
        },
        {
            test: /\.json$/,
            use: 'json-loader'
        }
    ]
};
config.plugins = [];
if (process.env.NODE_ENV !== 'production') {
    if (argv.watch) {
      config.plugins.push(new DashboardPlugin());
    }
}

config.node = {
    net: "empty",
    tls: "empty",
    dns: "empty"
};

// Production settings
if (process.env.NODE_ENV === 'production') {
    // config.entry = {
    //     survey: './build/static/js/app/survey.js',
    //     generate: './build/static/js/app/generate-survey.js'
    // };
    // config.output = {
    //     path: 'build/static/js',
    //     filename: '[name].js'  // TODO: Add the file hashing as well as the HTML altering webpack plugin
    // };
}
