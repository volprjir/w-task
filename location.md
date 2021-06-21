# Coding test

## About this task
~~~~~~**``**~~~~~~
Think of this as an open source project. How would this have to look in order for you to be impressed with it, if you were to find it on GitHub? Now go and do that.

Please spend at least 90 minutes on this test. Feel free to take more time if you wish - make sure you are happy with your submission!

_Hint_: we are looking for a high-quality submission with great application architecture. Not a "get it done" approach. Stay away from frameworks and boilerplates that handle everything for you. If you do use a framework, only use it as a thin layer so we can see how you structure applications yourself.  

_Hint2_: code your own constructs and 2 very general reusable methods you use over and over again.

_Hint3_: don't over comment the code, if code is properly done should be self-explanatory. Use function names whose meaning is obvious and clear from a glance at the name.

Remember that this test is your opportunity to show us how you think. Be clear about how you make decisions in your code, whether that is with comments, tests, or how you name things.

## What to do

### First

* Create a new Python-based application (no framework is better, if you use a framework use Tornado or Falcon)

### Task 1
* Render the list of stores from the `stores.json` file in alphabetical order using a template.
* Use postcodes.io to get the latitude and longitude for each postcode. Render them next to each store location in the template.
* Build the functionality that allows you to return a list of stores in a given radius of a given postcode in the UK. The list must be ordered from north to south. No need to render anything, but the function needs to be unit tested.

### Task 2
* Build an API that returns stores from the `stores.json` file, based on a given search string and unit test it. For example, return "Newhaven" when searching for "hav". Make sure the search allows to use both city name and postcode.
* Order the results by matching postcode first and then matching city names. For example, "br" would have "Orpington" as the 1st result as its postcode is "BR5 3RP". Next would be "Bracknell", "Broadstairs", "Tunbridge_Wells", and "Brentford"
* Using your favourite frontend framework on the user-facing side:
  * Build a frontend that renders a text field for the query and the list of stores that match it
  * Add suggestions to the query field as you type, with a debounce effect of 100ms and a minimum of 2 characters
  * Limit the results to 3 and lazy load the rest on page scroll

### Finally

* Zip your code up and send it back to us or send us a link to your repository.
* Provide answers for the following questions with your submission:
  1. If you had chosen to spend more time on this test, what would you have done differently?
      1(bis). Make sure you indicate the time you have spent in the README.md file among other metadata.
  2. What part did you find the hardest? What part are you most proud of? In both cases, why?
  3. What is one thing we could do to improve this test?
