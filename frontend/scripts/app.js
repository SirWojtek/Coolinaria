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
				'ngTouch',  'angucomplete' ]).constant('conf', {
	mockHTTP : true,
	searchURL : '/search',
	postReceipeURL : '/receipe/id',
}).config(function($routeProvider) {
	$routeProvider.when('/', {
		templateUrl : 'views/main.html',
		controller : 'MainCtrl'
	}).when('/login', {
		templateUrl : 'views/login.html',
		controller : 'LoginCtrl'
	}).when('/about', {
		templateUrl : 'views/about.html',
		controller : 'AboutCtrl'
	}).when('/receipe/:receipeId', {
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
	}).otherwise({
		redirectTo : '/'
	});
})/*.factory('sessionInjector', ['SessionService', function(SessionService) {  
    var sessionInjector = {
        request: function(config) {
            if (!SessionService.isAnonymus) {
                config.headers['x-session-token'] = SessionService.token;
            }
            return config;
        }
    };
    return sessionInjector;
}])*/.config(['$httpProvider', function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$httpProvider.defaults.headers.common['X-Requested-With' ]= 'XMLHttpRequest';
    //$httpProvider.interceptors.push('sessionInjector');
}]);
