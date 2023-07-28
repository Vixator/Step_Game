var geoip = require('geoip-lite');

var ip = "144.92.122.187";
var geo = geoip.lookup(ip);

if (geo) {
  console.log("Geolocation data for IP:", ip);
  console.log("Country:", geo.country);
  console.log("Region:", geo.region);
  console.log("City:", geo.city);
  console.log("Latitude:", geo.ll[0]);
  console.log("Longitude:", geo.ll[1]);
} else {
  console.log("Geolocation data not found for IP:", ip);
}
 