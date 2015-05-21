'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:SubmitReceipeCtrl
 * @description # SubmitReceipeCtrl Controller of the frontApp
 */
angular.module('frontApp').controller('SubmitReceipeCtrl', function($scope, $http) {

	$scope.awesomeThings = [ 'HTML5 Boilerplate', 'AngularJS', 'Karma' ];

	var uploadUrl = "http://192.168.50.2:8000/recipe/new/"
	
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

	$scope.addNewLine = function() {
		$scope.recipe.ingredients.push({
			name : "",
			amount : ""
		});
	}

	$scope.removeIngredient = function(i) {
		var index = $scope.recipe.ingredients.indexOf(i);
		if (index != -1) {
			$scope.recipe.ingredients.splice(index, 1);
		}
	}

	$scope.recipe = {
		name : "Omlet z omletem",
		description : "Fajny omlecik",
		type: ["breakfast"],
		ingredients : [ {
			name : "Woda",
			amount : "3 litry"
		}, {
			name : "Koks",
			amount : "300 gram"
		} ],
		instructions : "Weź 300 gram koksu\nPodgrzej z wodą\nBIERZ!"
	}

	var toFormula = function(description, instructions)
	{
		var formula = "";
		formula = formula.concat(description).concat('\n').concat(instructions);
		return formula;
	}
	
	$scope.uploadFile = function(files) {
	    var fd = new FormData();
	    //Take the first selected file
	    fd.append("file", files[0]);
	    
	    $scope.recipe.formula = toFormula($scope.recipe.description, $scope.recipe.instructions);
	    $scope.recipe.description = undefined;
	    $scope.recipe.instructions = undefined;
	    $scope.recipe.author = "admin@admin.pl";
	    $scope.recipe.duration = '3 szybkie minutki';
	    $scope.recipe.difficulty = 'hard';
	    
	    //TODO: Dodać duration i difficulcy, poprawić authora (a w zasadzie dodać CSRF i sessionToken)
	    
	    
	    fd.append("recipe", angular.toJson($scope.recipe));
	    
	    $http.post(uploadUrl, fd, {
	        //withCredentials: true,
	        headers: {'Content-Type': undefined },
	        transformRequest: angular.identity
	    }).success(function(){
	    	console.log("UPLOAD OK!");
	    }).error(function(err){
	    	console.log("ERROR!");
	    	console.log(err);
	    } );

	};
	
	$scope.submitRecipe = function(r) {
		console.log(r);
		
		
		
	}

});
