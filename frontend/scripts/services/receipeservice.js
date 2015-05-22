'use strict';

/**
 * @ngdoc service
 * @name frontApp.receipeService
 * @description # receipeService Service in the frontApp.
 */
angular
		.module('frontApp')
		.service(
				'receipeService',
				[
						'conf',
						'$http',
						'$httpBackend',
						'$q',
						function(conf, $http, $httpBackend, $q) {

							var searchResults = undefined;
							var receipeSearch = 'http://156.17.42.126:1280/recipe/search/';
							var receipeGet = 'http://156.17.42.126:1280/recipe/get/';

							this.search = function(ingredient, types) {
								console.log("Search");
								return $q(function(resolve, reject) {
									$http.post(receipeSearch, {
										ingredient : ingredient,
										type : types
									}).success(function(data) {
										searchResults = data;
										resolve(searchResults);
									}).error(function(err) {
										searchResults = undefined;
										reject(searchResults);
									});

								});

							};

							this.getReceipeByID = function(id) {								
								return $q(function(resolve, reject) {
									$http.get(receipeGet + id + '/')
											.success(function(data) {
												
												//Preparsing please...
												
												
												
												console.log(data);
												resolve(data);
											}).error(function(err) {
												reject(err);
											});
								});
							};

							this.getSearchResults = function() {
								return searchResults;
							}

						} ]);
