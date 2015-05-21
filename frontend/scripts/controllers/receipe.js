'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:ReceipectrlCtrl
 * @description
 * # ReceipectrlCtrl
 * Controller of the frontApp
 */
angular.module('frontApp')
  .controller('ReceipeCtrl', function ($scope, $routeParams, receipeService) {
  
	  $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
	  console.log("receipeID:");
	  console.log($routeParams.receipeId)
	  receipeService.getReceipeByID($routeParams.receipeId).then(function(receipe){
		  $scope.dish = receipe; 
	  }, function(err){
		  $scope.errorMsg = "Invalid receipe specified!";
	  });    	  
	  
  });
