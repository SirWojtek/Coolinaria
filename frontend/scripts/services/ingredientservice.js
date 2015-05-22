'use strict';

/**
 * @ngdoc service
 * @name frontApp.ingredientService
 * @description # ingredientService Service in the frontApp.
 */
angular.module('frontApp').service('ingredientService', function($http, $q) {
	// AngularJS will instantiate a singleton by calling "new" on this function

	var _ingredients = undefined;
	var ingredientEndpoint = 'http://156.17.42.126:1280/ingredient/';

	this.reloadIngredients = function() {
		// TODO: To be implemented
	}

	this.getIngredients = function() {
		return $q(function(resolve, reject) {

			$http.get(ingredientEndpoint).success(function(data) {
				console.log("Ingredients get! Data:")
				console.log(data);
				_ingredients = data;
				resolve(data);
			}).error(function(err) {
				_ingredients = undefined;
				reject(_ingredients);				
			});
		});
	}

});
