'use strict';

describe('Controller: ReceipectrlCtrl', function () {

  // load the controller's module
  beforeEach(module('frontApp'));

  var ReceipectrlCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ReceipectrlCtrl = $controller('ReceipeCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
