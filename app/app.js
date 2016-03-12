var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var routes = require('./routes/index');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'client', 'views'));

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use('/views',  express.static(__dirname + '/client/views'));
app.use('/scripts', express.static(__dirname + '/client/public/javascripts'));
app.use('/css',  express.static(__dirname + '/client/public/stylesheets'));
app.use('/bower_components',  express.static(__dirname + '/bower_components'));

app.use('/', routes);

module.exports = app;
