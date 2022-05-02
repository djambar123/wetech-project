from Setup import *
import unittest


class UI_Syllabus(Setup, unittest.TestCase):

    driver = None

    # Execute before all test methode
    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver

    def test_html(self):
        HTML = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[3]/div[1]/ul[1]/ul[1]/li[1]"
        TITLE= "//h1[contains(text(),'HTML')]"

        sleep(3)
        # clicking on html link
        self.driver.find_element(By.XPATH,HTML).click()
        # html title
        title = self.driver.find_element(By.XPATH, TITLE).get_attribute("innerText")
        # html link
        html_link = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]").get_attribute("innerText")

        assert title == "HTML" and html_link == "HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and " \
                            "structure of web content. Other technologies besides HTML are generally used to describe a web page's " \
                            "appearance/presentation (CSS) or functionality/behavior (JavaScript).\n\n\"Hypertext\" refers to links that " \
                            "connect web pages to one another, either within a single website or between websites. Links are a fundamental " \
                            "aspect of the Web. By uploading content to the Internet and linking it to pages created by other people, you " \
                            "become an active participant in the World Wide Web.\n\nHTML uses \"markup\" to annotate text, images, and other " \
                            "content for display in a Web browser. HTML markup includes special \"elements\" such as head, title, body, header" \
                            ", footer, article, section, p, div, span, img, aside, audio, canvas, datalist, details, embed, nav, output, " \
                            "progress, video, ul, ol, li and many others.\n\nAn HTML element is set off from other text in a document by " \
                            "\"tags\", which consist of the element name surrounded by and . The name of an element inside a tag is case " \
                            "insensitive. That is, it can be written in uppercase, lowercase, or a mixture. For example, the title tag can be" \
                            " written as Title, TITLE, or in any other way."


    def test_css(self):
        sleep(3)
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[3]/div[1]/ul[1]/ul[1]/li[2]").click()
        # css title
        title = self.driver.find_element(By.XPATH, "//h1[contains(text(),'CSS')]").get_attribute("innerText")
        # css link
        css_link = self.driver.find_element_by_tag_name("SECTION").get_attribute("innerText")
        sleep(3)
        assert title == "CSS" and css_link == "Cascading Style Sheets (CSS) is a stylesheet language used to describe the presentation of a document written" \
                            " in HTML or XML (including XML dialects such as SVG, MathML or XHTML). CSS describes how elements should be " \
                            "rendered on screen, on paper, in speech, or on other media.\n\nCSS is among the core languages of the open web" \
                            " and is standardized across Web browsers according to W3C specifications. Previously, development of various " \
                            "parts of CSS specification\n\nwas done synchronously, which allowed versioning of the latest recommendations. " \
                            "You might have heard about CSS1, CSS2.1, CSS3. However, CSS4 has never become an official version.\n\nFrom" \
                            " CSS3, the scope of the specification increased significantly and the progress on different CSS modules started" \
                            " to differ so much, that it became more effective to develop and release recommendations separately per module." \
                            " Instead of versioning the CSS specification, W3C now periodically takes a snapshot of the latest stable state" \
                            " of the CSS specification"

    def test_java_script(self):
        sleep(3)
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[3]/div[1]/ul[1]/ul[1]/li[3]").click()
        # java script title
        title = self.driver.find_element(By.XPATH, "//h1[contains(text(),'JavaScript')]").get_attribute("innerText")
        # java script link
        java_script_link = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]").get_attribute(
            "innerText")

        assert title == "JavaScript" and java_script_link == "JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class" \
                                                             " functions. While it is most well-known as the scripting language for Web pages, many non-browser environments" \
                                                             " also use it, such as Node.js, Apache CouchDB and Adobe Acrobat. JavaScript is a prototype-based, multi-paradigm," \
                                                             " single-threaded, dynamic language, supporting object-oriented, imperative, and declarative (e.g. functional " \
                                                             "programming) styles. Read more about JavaScript.\n\nThis section is dedicated to the JavaScript language itself," \
                                                             " and not the parts that are specific to Web pages or other host environments. For information about API " \
                                                             "specifics to Web pages, please see Web APIs and DOM.\n\nThe standards for JavaScript are the ECMAScript Language" \
                                                             " Specification (ECMA-262) and the ECMAScript Internationalization API specification (ECMA-402). The JavaScript " \
                                                             "documentation throughout MDN is based on the latest draft versions of ECMA-262 and ECMA-402. And in cases where " \
                                                             "some proposals for new ECMAScript features have already been implemented in browsers, documentation and examples" \
                                                             " in MDN articles may use some of those new features.\n\nDo not confuse JavaScript with the Java programming " \
                                                             "language. Both \"Java\" and \"JavaScript\" are trademarks or registered trademarks of Oracle in the U.S. and " \
                                                             "other countries. However, the two programming languages have very different syntax, semantics, and use."

    def test_footer(self):
        sleep(3)
        footer = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[3]/div[1]").get_attribute("innerText")
        assert footer == "all rights deserve to our Full-Stack developers\nEden Genet Tasama\nAmir Mangisto\nHaim Ayenow"

    # Execute after all test methode
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
