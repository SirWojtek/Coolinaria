'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:FindCtrl
 * @description
 * # FindCtrl
 * Controller of the frontApp
 */
angular.module('frontApp')
  .controller('FindCtrl', function ($scope, $routeParams, $location, $timeout) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    
    console.log("RouteParams:")
    console.log($routeParams)
    
     $scope.search = function(item)
    {
    	$scope.searchResults = $scope.results;       	
    }
    
    $scope.receipe = function(item)
    {    	
    	$location.path("receipe")
    }
    
    $scope.ingredientList = [{name: 'kalafior'},{name: 'kalafior2'},{name: 'kalafior3'}, {name:'marchew'}];
     
    $scope.ingredients = [{description:"Brokuły", img: "images/food/brokuly.jpg", target: $scope.search},
                          {description:"Szpinak", img: "images/food/szpinak.jpg", target: $scope.search},
                          {description:"Kurczak", img: "images/food/kurczak.jpg", target: $scope.search},
                          {description:"Kalarepa", img: "images/food/kalarepa.jpg", target: $scope.search},
                          {description:"Marchew", img: "images/food/marchew.jpg", target: $scope.search},
                          {description:"Pietruszka", img: "images/food/pietruszka.jpg", target: $scope.search},
                          {description:"Wołowina", img: "images/food/wolowina.jpg", target: $scope.search},
                          {description:"Rzepa", img: "images/food/rzepa.jpg", target: $scope.search}
                          ];
    
    $scope.results = [
                            {description: "Makaron z brokułami", img:"images/dish/makaron_z_brokulami.jpg", target: $scope.receipe},
                            {description: "Makaron ze szpinakiem", img:"images/dish/makaron_ze_szpinakiem.jpg", target: $scope.receipe},
                            {description: "Kurczak w ziołach", img:"images/dish/kurczak_w_ziolach.jpg", target: $scope.receipe},
                            {description: "Zapiekanka cygańska", img:"images/dish/zapiekanka_cyganska.jpg", target: $scope.receipe},
                            {description: "Pierogi ruskie", img:"images/dish/pierogi_ruskie.jpg", target: $scope.receipe},
                            {description: "Gołąbki tradycyjne", img:"images/dish/golabki_tradycyjne.jpg", target: $scope.receipe},
                            {description: "Kluski śląskie", img:"images/dish/kluski_slaskie.jpg", target: $scope.receipe},
                            {description: "Kasza z warzywami", img:"images/dish/kasza_z_warzywami.jpg", target: $scope.receipe}
    						];
	
   
   $scope.searchResults = $scope.ingredients; 
    
    
  });
