from bs4 import BeautifulSoup as but
import requests
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/",methods=["GET"])
def bike():
    return render_template("bike.html")

@app.route("/bike",methods=["GET","POST"])
def bike_1():
    if request.method=="POST":
        try:
            search=request.form["text"].replace(" ","-")                              #hero
            ser=request.form["text1"].replace(" ","-")                                #spendor

            searchall=search+"-bikes/"+ser
            print(searchall)
            bikelink = "https://www.bikewale.com/"+searchall
            bikeDetails = requests.get(bikelink)
            bike_html = but(bikeDetails.text, "html.parser")
            bikeReview = bike_html.find_all("ul", class_="user-review-list")
            # print(bikeReview)
            bike_info=[]
            # print(bike_html)
            for bikes_1 in bikeReview:
                # print(bikes_1)
                try:
                    bikename=bike_html.find_all("h1",{"class":"page-header"})[0].text
                except:
                    bikename=" bike name is not availble"
                try:
                    bikerating=bike_html.find_all("span", class_="font14 text-bold inline-block")[0].text
                except:
                    bikerating=" bike rating is not avilable"
                try:
                    bikeprice = bike_html.find_all("span", class_="font22 font-bold")[0].text
                except:
                    bikeprice = " bike price not available"
                try:
                    bikeMilage = bike_html.find_all("ul", class_="inline-block")
                    bikeMilage_1 = bikeMilage[0].find_all("li")[1].text
                except:
                    bikeMilage_1=" bike milage not available"
                try:
                    bikeReview1 =bikes_1.find_all("span", class_="rating-badge")[0]
                    bikeReviewRating = bikeReview1.find_all("span")[1].text
                except:
                    bikeReviewRating=" bike_html rating is not availble"
                try:
                    BikeHeadingReview= bikes_1.find_all("span",class_="list-item-title inline-block margin-right5")[0].text
                except:
                    BikeHeadingReview=" review heading not avilable"
                try:
                    bikeReviewerName =bikes_1.find_all("span", class_="font12 inline-block text-light-grey")[0].text
                except:
                    bikeReviewerName = " bike reviwes not available"
                try:
                    BikeReviewContent = bikes_1.find_all("div", class_="main-content")[0].p.text
                except:
                    BikeReviewContent =" bike review content not avavilable "

                bike_in={"bikename":bikename,"bikerating":bikerating,"bikeprice":bikeprice,"bikeMilage_1":bikeMilage_1,"bikeReviewRating":bikeReviewRating,"BikeHeadingReview":BikeHeadingReview,"bikeReviewerName":bikeReviewerName,"BikeReviewContent":BikeReviewContent
                        }
                bike_info.append(bike_in)
                print(bike_info)
            return render_template("result.html",reviews=bike_info[0:1] )
        except:
            return "p"

















app.run()