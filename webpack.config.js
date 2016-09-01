const webpack = require('webpack');

const config = {};
config.entry = {
    survey: './src/static/js/app/survey.js',
    generate: './src/static/js/app/generate-survey.js'
};
config.output = {
    path: 'src/static/js',
    filename: '[name].js'
};
config.module = {
    loaders: [
        {
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
            query: {
                presets: ['es2015', 'react'],
                plugins: ['transform-class-properties']
            }
        },
        {
            test: /\.json$/,
            loader: 'json'
        }
    ]
};
config.plugins = [
     new webpack.ProvidePlugin({
        'Promise': 'imports?this=>global!exports?global.Promise!es6-promise',
        'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
     })
];
config.node = {
    net: "empty",
    tls: "empty",
    dns: "empty"
};

// Production settings
if (process.env.NODE_ENV === 'production') {
    config.entry = {
        survey: './build/static/js/app/survey.js',
        generate: './build/static/js/app/generate-survey.js'
    };
    config.output = {
        path: 'build/static/js',
        filename: '[name].js'
    };
}

module.exports = config;
