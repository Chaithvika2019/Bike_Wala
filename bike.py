from bs4 import BeautifulSoup as but
                                             # this is one module
import requests
                                             # this is one module
from flask import Flask,render_template,request
                                                # this is onother module

app=Flask(__name__)
@app.route("/",methods=["GET"])
def bike():
    return render_template("bike.html")

@app.route("/bike",methods=["GET","POST"])
                                                   # these are methods to use
def bike_1():
    if request.method=="POST":
        try:
            search=request.form["text"].replace(" ","-")                              #hero
            ser=request.form["text1"].replace(" ","-")                                #splendor

            searchall=search+"-bikes/"+ser.lower()
                                                                                   # this line for common names in search
            print(searchall)
                                                                                       # this line for to see output
            bikelink = "https://www.bikewale.com/"+searchall
                                                                                         # this line is webpage link
            bikeDetails = requests.get(bikelink)
                                                                                         # this line for to get bike link
            bike_html = but(bikeDetails.text, "html.parser")
            bikeReview = bike_html.find_all("ul", class_="user-review-list")
                                                                                        # this line for to see bikeReviews
            # print(bikeReview)
                                                                                        # this line for create list
            # print(bike_html)
            for bikes_1 in bikeReview:
                bike_info = []
                # in this line use for loop
                # print(bikes_1)
                try:
                    bikename=bike_html.find_all("h1",{"class":"page-header"})[0].text
                                                                                          # this line for find BikeName
                except:
                    bikename=" bike name is not availble"
                try:
                    bikerating=bike_html.find_all("span", class_="font14 text-bold inline-block")[0].text
                                                                                                    # this line for find BikeRating
                except:
                    bikerating=" bike rating is not avilable"
                try:
                    bikeprice = bike_html.find_all("span", class_="font22 font-bold")[0].text
                                                                                                           # this line for find BikePrice
                except:
                    bikeprice = " bike price not available"
                try:
                    bikeMilage = bike_html.find_all("ul", class_="inline-block")
                                                                                      # this line for BikeMilage
                    bikeMilage_1 = bikeMilage[0].find_all("li")[1].text
                except:
                    bikeMilage_1=" bike milage not available"
                try:
                    bikeReview1 =bikes_1.find_all("span", class_="rating-badge")[0]
                                                                                         # this line for BikeReview
                    bikeReviewRating = bikeReview1.find_all("span")[1].text
                except:
                    bikeReviewRating=" bike_html rating is not availble"
                try:
                    BikeHeadingReview= bikes_1.find_all("span",class_="list-item-title inline-block margin-right5")[0].text
                                                                                                                           # this line for find BikeHeadingReview
                except:
                    BikeHeadingReview=" review heading not avilable"
                try:
                    bikeReviewerName =bikes_1.find_all("span", class_="font12 inline-block text-light-grey")[0].text
                                                                                                                        # this line for find reveivername
                except:
                    bikeReviewerName = " bike reviwes not available"
                try:
                    BikeReviewContent = bikes_1.find_all("div", class_="main-content")[0].p.text
                                                                                                   # this line for to find ReviewContent
                except:
                    BikeReviewContent =" bike review content not avavilable "
                bike_in={"bikename":bikename,"bikerating":bikerating,"bikeprice":bikeprice,"bikeMilage_1":bikeMilage_1,"bikeReviewRating":bikeReviewRating,"BikeHeadingReview":BikeHeadingReview,"bikeReviewerName":bikeReviewerName,"BikeReviewContent":BikeReviewContent}                                                                       # this line for to create dictionary
                bike_info.append(bike_in)                                                                        # this line for appending the dictionary
                print(bike_info)
            return render_template("result.html",review=bike_info[0:1] )
        except:
            return "p"

















app.run()