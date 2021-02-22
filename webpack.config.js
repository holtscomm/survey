const webpack = require('webpack');
const argv = require('yargs').argv;
const path = require('path');

const config = {};
module.exports = config;

config.mode = 'development';
config.devtool = 'eval-cheap-source-map';
config.entry = {
    survey: './src/static/js/app/survey.js',
    generate: './src/static/js/app/generate-survey.tsx',
};
config.output = {
    path: path.resolve(__dirname, 'src/static/js'),
    filename: '[name].js',
    publicPath: '/static/js/'
};
config.resolve = {
    // "alias": {  // Disabled for now, until I figure out what's up with UglifyJS and punc())s
    //     "react": "preact-compat",
    //     "react-dom": "preact-compat"
    // }
    extensions: ['.tsx', '.ts', '.js'],
};
config.module = {
    rules: [
        {
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
        },
        {
            test: /\.tsx?$/,
            use: 'ts-loader',
            exclude: /node_modules/,
        },
        {
            test: /\.json$/,
            use: 'json-loader'
        }
    ]
};

// Production settings
if (process.env.NODE_ENV === 'production') {
    config.entry = {
        survey: './build/static/js/app/survey.js',
        generate: './build/static/js/app/generate-survey.tsx',
    };
    config.output = {
        path: path.resolve(__dirname, './build/static/js'),
        filename: '[name].js'  // TODO: Add the file hashing as well as the HTML altering webpack plugin
    };
    config.mode = 'production';
}
