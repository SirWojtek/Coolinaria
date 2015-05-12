'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:LoginCtrl
 * @description # LoginCtrl Controller of the frontApp
 */
angular.module('frontApp')
  .controller('LoginCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    
  }).directive('applyUniform', function () {
	    return {
	        restrict: 'A',
	        /*link: function(scope, element, attr, ngModel) {
	            element.uniform({useID: false});
	            scope.$watch(function() {return ngModel.$modelValue}, function() {
	              $timeout(jQuery.uniform.update, 0);
	            } );
	          }*/
	        };
	      });
