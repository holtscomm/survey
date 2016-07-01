const webpack = require('webpack');

module.exports = {
    entry: './src/static/js/app/survey.js',
    output: {
        filename: 'src/static/js/survey.js'
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
