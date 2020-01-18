from urllib import request

if __name__ == "__main__":
    url = "http://10.247.0.11:8888/411624/serviceDispatcher.do?frc_code=411624&org_code=4116240154&key=64944779D4FADBC5D6A123783E23E3D9&password=60B6412F90927EE14AACFF3667E2A19A938BFDA3A1CDE646&funccode=100102&i102_01=0154&f_param="

    rsp = request.urlopen(url)

    html = rsp.read().decode()

    file = open("out.html", mode="w")

    file.write(html)