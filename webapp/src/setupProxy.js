/* eslint-disable no-undef */
module.exports = function (app) {
    app.use(proxy(`/auth/**`, { 
        target: 'http://localhost:5001' 
    }));
};