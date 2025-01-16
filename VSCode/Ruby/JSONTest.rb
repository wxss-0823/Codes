require 'rubygems'
require 'json'
require 'pp'

json = File.read('JSONTest.json')
obj = JSON.parse(json)

obj.each {
  |item| item.each {
    |item| pp item
  }
}