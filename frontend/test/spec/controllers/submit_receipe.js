'use strict';

describe('Controller: SubmitReceipeCtrl', function () {

  // load the controller's module
  beforeEach(module('frontApp'));

  var SubmitReceipeCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    SubmitReceipeCtrl = $controller('SubmitReceipeCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
