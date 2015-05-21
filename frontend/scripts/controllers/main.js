'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontApp
 */
angular.module('frontApp')
  .controller('MainCtrl', function ($scope, $location) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    
	$scope.types = [ {
		"name" : "Śniadania",
		"id" : "breakfast"
	}, {
		"name" : "Obiady",
		"id" : "dinner"
	}, {
		"name" : "Kolacje",
		"id" : "supper"
	}, {
		"name" : "Desery",
		"id" : "dessert"
	}, {
		"name" : "Przekąski",
		"id" : "snack"
	}, ]; 
    
	$scope.selectedType = $scope.types[0].id;
	
	$scope.search = function(searchVal)
	{
		$location.path('find').search({ingredient: searchVal, types: $scope.selectedType});		
	}
	
  });
