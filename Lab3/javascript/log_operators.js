alert(null || 2 || undefined); // 2

alert(alert(1) || 2 || alert(3)); // 1 then 2

alert(1 && null && 2); // null

alert(alert(1) && alert(2)); // 1 then undefined

alert(null || (2 && 3) || 4); // 3

if (age >= 14 && age <= 90); // Check the range between

if (age < 14 || age > 90); // Check the range outside

// Runs.
// The result of -1 || 0 = -1, truthy
if (-1 || 0) alert("first");

// Doesn't run
// -1 && 0 = 0, falsy
if (-1 && 0) alert("second");

