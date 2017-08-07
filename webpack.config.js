const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')

module.exports = {
	entry: [
		path.join(__dirname, 'app/index.jsx'),
		'react-hot-loader/patch',
		'babel-polyfill'
	],
	resolve: {
		extensions: [".js", ".jsx", ".json"]
	},
	output: {
		path: path.join(__dirname, '/static/'),
		filename: '[name].js',
		publicPath: '/'
	},
	devtool: 'inline-source-map',
	devServer: {
		contentBase: './static/',
		hot: true,
		host: '0.0.0.0',
		disableHostCheck: true,
		proxy: {
			"/api": {
				target: "http://flask:5000",
				pathRewrite: {"^/api": ""}
			}
		}
	},
	plugins: [
		new CleanWebpackPlugin(['static']),
		new HtmlWebpackPlugin({
			template: 'app/index.tpl.html',
			inject: 'body',
			filename: 'index.html'
		}),
		new webpack.HotModuleReplacementPlugin()
	],
	module: {
		loaders: [
			{
				test: /\.jsx?$/,
				exclude: /node_modules/,
				use: [
					'react-hot-loader/webpack',
					{
						loader: 'babel-loader',
						options: {
							presets: ['react', 'es2015']
						}
					}
				]
			}
		]
	}
}
