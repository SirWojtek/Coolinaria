'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:LoginCtrl
 * @description # LoginCtrl Controller of the frontApp
 */
angular.module('frontApp')
  .controller('LoginCtrl', function ($scope, $location, loginService) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    
    $scope.loginButton = function(user, password)
    {
    	loginService.login(user, password).then(function(isAdmin){
    		console.log("Login returned. Admin status:");
    		console.log(isAdmin);
    		$location.path(find);
    	}, function(error){
    		$scope.errorMessage = "Invalid credentials!";
    	})
    	
    }
    
  });
