'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:ReceipectrlCtrl
 * @description
 * # ReceipectrlCtrl
 * Controller of the frontApp
 */
angular.module('frontApp')
  .controller('ReceipeCtrl', function ($scope) {
  
	  $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    
    $scope.dish = {
    		img: 'images/dish/makaron_ze_szpinakiem.jpg',
    		title: 'Makaron ze szpinakiem',
    		ingredients: [
    		              {name: 'Makaron', amount: '300g'},
    		              {name: 'Szpinak', amount: '1 opakowanie'},
    		              {name: 'Śmietana', amount: '1 duża (250g)'},
    		              {name: 'Czosnek', amount: '3 ząbki'},
    		              {name: 'Masło', amount:'1 łyżka'}
    		              ],
    		description: 'Makaron ze szpinakiem w sosie śmietanowo- serowym. Bardzo szybkie danie, a jakże zdrowe. Polecam użyć świeży szpinak, ale jeśli jest on akurat niedostępny to może to być również szpinak mrożony (najlepiej listki, a nie siekany).Doprawiając sos można dodać odrobinę soli, ale należy uważać, bo ser feta jest mocno słony.',
    		steps: [{text:'Ser feta pokroić w małą kostkę. Odstawić na bok.'},{text:'Szpinak opłukać i oderwać twarde łodyżki. (Mrożony rozmrozić i odcisnąć wodę).'},
    		        {text:'Makaron ugotować al dente według przepisu na opakowaniu.'},{text:'Na dużej patelni rozgrzać masło. Dodać posiekany (lub przeciśnięty przez prasę) czosnek. Podsmażyć chwilkę. Dodać szpinak i smażyć, aż straci objętość. Dodać śmietanę i ser feta. Mieszać, aż ser się rozpuści. Doprawić pieprzem do smaku.'},
    		        {text:'Makaron rozłożyć na talerze, a na górę ułożyć szpinak z sosem albo makaron wymieszać ze szpinakiem na patelni.'}, {text:'Podawać od razu.'}]    		
    };
    
  });
