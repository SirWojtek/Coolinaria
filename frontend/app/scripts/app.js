'use strict';

/**
 * @ngdoc overview
 * @name frontApp
 * @description
 * # frontApp
 *
 * Main module of the application.
 */
angular.module(
		'frontApp',
		[ 'ngAnimate', 'ngCookies', 'ngResource', 'ngRoute', 'ngSanitize',
				'ngTouch', 'angucomplete']).config(function($routeProvider) {
	$routeProvider.when('/', {
		templateUrl : 'views/main.html',
		controller : 'MainCtrl'
	}).when('/login', {
		templateUrl : 'views/login.html',
		controller : 'LoginCtrl'
	}).when('/about', {
		templateUrl : 'views/about.html',
		controller : 'AboutCtrl'
	}).when('/receipe', {
		templateUrl : 'views/receipe.html',
		controller : 'ReceipeCtrl'
	}).when('/contact', {
		templateUrl : 'views/contact.html',
		controller : 'ContactCtrl'
	}).when('/submit', {
		templateUrl : 'views/submit_recipe.html',
		controller : 'SubmitReceipeCtrl'
	}).when('/find', {
		templateUrl : 'views/find.html',
		controller : 'FindCtrl'
	}).when('/find/:ingredient', {
		templateUrl : 'views/find.html',
		controller : 'FindCtrl'
	}).otherwise({
		redirectTo : '/'
	});
});
