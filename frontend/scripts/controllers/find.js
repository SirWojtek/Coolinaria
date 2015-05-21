'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:FindCtrl
 * @description # FindCtrl Controller of the frontApp
 */
angular
		.module('frontApp')
		.controller(
				'FindCtrl',
				function($scope, $routeParams, $location, receipeService,
						ingredientService) {
					$scope.awesomeThings = [ 'HTML5 Boilerplate', 'AngularJS',
							'Karma' ];

					var getTypes = function()
					{
						var types = [];
						for ( var key in $scope.selectedTypes.ids) {
							if ($scope.selectedTypes.ids.hasOwnProperty(key)) {
								if ($scope.selectedTypes.ids[key]) {
									types.push(key);
								}
							}
						}	
						return types;
					}					
					
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

					$scope.selectedTypes = {
						ids : {}
					};

					if ($location.search().types) {
						if (typeof ($location.search().types) == 'string') {
							$scope.selectedTypes.ids[$location.search().types] = true;
						} else {
							$location.search().types.forEach(function(o) {
								$scope.selectedTypes.ids[o] = true;
							});
						}
					} else {
						$scope.types.forEach(function(o) {
							$scope.selectedTypes.ids[o.id] = true;
						});
					}

					console.log($scope.selectedTypes);
					
					if ($location.search().ingredient
							|| $location.search().types) {
						$scope.selectReceipe = true;	
						var types = getTypes();
						receipeService.search($location.search().ingredient,
								types).then(function(data) {
							$scope.searchResults = data;
						});
					} else {
						$scope.selectReceipe = false;
					}

					$scope.squareClicked = function(square) {
						if (!$scope.selectReceipe) {
							$location.search({
								ingredient : square.name
							});
						} else {
							$location.path('receipe/' + square.id).search({});
						}
					};

					$scope.receipe = function() {

					};

					$scope.search = function() {
						console.log($scope.selectedIngredient.title);
						console.log($scope.selectedTypes);
						var types = getTypes();
						$location.search({
							ingredient : $scope.selectedIngredient.title,
							types : types
						});
					}

					ingredientService.getIngredients().then(function(data){
						$scope.ingredients = data;
						$scope.searchResults = $scope.ingredients;
					}, function(err){
						$scope.ingredients = undefined;
					});
					
					$scope.searchResults = $scope.ingredients;


				});
