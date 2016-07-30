const webpack = require('webpack');

module.exports = {
    entry: {
        survey: './src/static/js/app/survey.js',
        generate: './src/static/js/app/generate-survey.js'
    },
    output: {
        path: 'src/static/js',
        filename: '[name].js'
    },
    module: {
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
    },
    plugins: [
         new webpack.ProvidePlugin({
            'Promise': 'imports?this=>global!exports?global.Promise!es6-promise',
            'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
         })
    ],
    node: {
        net: "empty",
        tls: "empty",
        dns: "empty"
    }
};
