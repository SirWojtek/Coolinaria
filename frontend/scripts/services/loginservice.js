'use strict';

/**
 * @ngdoc service
 * @name frontApp.loginService
 * @description # loginService Service in the frontApp.
 */
angular.module('frontApp').service('loginService',
		[ '$q', '$http', function($q, $http) {
			var _logged = false;
			var _isModerator = false;
			var loginEndpoint = 'http://156.17.42.126:1280/account/login/';
			var logoutEndpoint = 'http://api.mydomain.com/logout/';

			this.sayHello = function() {
				return 'Hello, World!';
			};

			this.login = function(username, password) {
				return $q(function(resolve, reject) {
					$http.post(loginEndpoint, {
						email : username,
						password : password
					}).success(function(data, status, headers, config) {
						switch (status) {
						case 200:
							//Here should get XCRF or sumfing
							_logged = true;
							if (data.isModerator === 'true') {
								_isModerator = true;
							} else {
								_isModerator = false; 
							}
							resolve({
								isModerator : _isModerator
							});
							break;
						case 220:
							_logged = false;
							reject('Invalid login data!');
						}
					}).error(function(data, status, headers, config) {
						reject(data);
					});
				});
			};
			
			this.logout = function()
			{
				_logged = false;
				$http.get(logoutEndpoint);				
			};

			this.loggedIn = function() {
				return _logged;
			};
		} ]);
