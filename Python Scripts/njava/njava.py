from pathlib import Path


# Creating new java file with it's name
def new_project(paths):
    try:
        java_file_id = open(paths, "x")
        java_file_id.close()
        return False
    except FileExistsError:
        print("Project file already created in this directory >>>")
        return True


# importing Libs (some libs aren't available)
def import_class(import_array, paths):
    java_file_id = open(paths, "a") 
    for strings in import_array:
        if strings == "scanner":
            java_file_id.write("import java.util.Scanner" + ";" + "\n")
        elif strings == "random" or strings == "rand":
            java_file_id.write("import java.util.Random" + ";" + "\n")
        elif strings == "calendar":
            java_file_id.write("import java.util.Calendar" + ";" + "\n")
        elif strings == "date":
            java_file_id.write("import java.util.Date" + ";" + "\n")
        elif strings == "dictionary":
            java_file_id.write("import java.util.Dictionary" + ";" + "\n")
        elif strings == "simpletimezone":
            java_file_id.write("import java.util.SimpleTimeZone" + ";" + "\n")
        elif strings == "timezone":
            java_file_id.write("import java.util.TimeZone" + ";" + "\n")
        elif strings == "observer":
            java_file_id.write("import java.util.Observer" + ";" + "\n")
        elif strings == "observable":
            java_file_id.write("import java.util.Observable" + ";" + "\n")
        elif strings == "properties":
            java_file_id.write("import java.util.Properties" + ";" + "\n")
        elif strings == "stack":
            java_file_id.write("import java.util.Stack" + ";" + "\n")
        elif strings == "vector":
            java_file_id.write("import java.util.Vector" + ";" + "\n")
        elif strings == "locale":
            java_file_id.write("import java.util.Locale" + ";" + "\n")
        elif strings == "emptystackexception":
            java_file_id.write("import java.util.EmptyStackException" + ";" + "\n")
        elif strings == "enumeration":
            java_file_id.write("import java.util.Enumeration" + ";" + "\n")
        elif strings == "eventlistener":
            java_file_id.write("import java.util.EventListener" + ";" + "\n")
        elif strings == "eventobject":
            java_file_id.write("import java.util.EventObject" + ";" + "\n")
        elif strings == "gregoriancalendar":
            java_file_id.write("import java.util.GregorianCalendar" + ";" + "\n")
        elif strings == "hashtable":
            java_file_id.write("import java.util.Hashtable" + ";" + "\n")
        elif strings == "listresourcebundle":
            java_file_id.write("import java.util.ListResourceBundle" + ";" + "\n")
        elif strings == "missingresorceexception":
            java_file_id.write("import java.util.MissingResourceException" + ";" + "\n")
        elif strings == "nosuchelementexception":
            java_file_id.write("import java.util.NoSuchElementException" + ";" + "\n")
        elif strings == "propertyresourcebundle":
            java_file_id.write("import java.util.PropertyResourceBundle" + ";" + "\n")
        elif strings == "resourcebundle":
            java_file_id.write("import java.util.ResourceBundle" + ";" + "\n")
        elif strings == "stringtokenizer":
            java_file_id.write("import java.StringTokenizer" + ";" + "\n")
        elif strings == "toomanylistenersexception":
            java_file_id.write("import java.TooManyListenersException" + ";" + "\n")
        else:
            java_file_id.write("// " + strings + " import here" + "\n")
    java_file_id.close()
    return True


# Creating main class and method
def main_class(names, paths):
    java_file_id = open(paths, "a")
    java_file_id.write("\n" + "class " + names + " {" + "\n")
    java_file_id.write("""
        static {  }
        public static void main(String[] args) {
            
                
        }
}""")
    java_file_id.close()
    return True


def new_class(names, paths):
    java_file_id = open(paths, "a")
    java_file_id.write("\n" + "class " + names + " {" + "\n")
    java_file_id.write("""
}""")
    java_file_id.close()
    return True


def new_interface(names, paths):
    java_file_id = open(paths, "a")
    java_file_id.write("\n" + "public interface " + names + " {" + "\n")
    java_file_id.write("""
}""")
    java_file_id.close()
    return True


def new_abstract(names, paths):
    java_file_id = open(paths, "a")
    java_file_id.write("\n" + "public abstract class " + names + " {" + "\n")
    java_file_id.write("""
    }""")
    java_file_id.close()
    return True


# input
print("""Available Java Packages
java.util
""")
print("HELP New Java Project <Type--Name>")
print("HELP Import <import1 import2>")
path_mode_string = input("New Java Project>>> ")
imports = input("Import>>> ")

# variable array
pms = path_mode_string.split("--")
path = Path.cwd()
mode = pms[0]
class_name = pms[1].capitalize()
name = pms[1].capitalize() + ".java"
imports_array = imports.split(" ")
right_path = ""
path_new = Path.joinpath(path, name)
isExist = new_project(path_new)
if isExist:
    input("Press any key to exit >>>>>>>>>>>>>>>>>>")
else:
    lib_complete = import_class(imports_array, path_new)
    if lib_complete:
        if mode == "class":
            complete = new_class(class_name, path_new)
            if complete:
                print(class_name + " " + mode + " Complete")
                input("Press any key to exit >>>")
        if mode == "main":
            complete = main_class(class_name, path_new)
            if complete:
                print(class_name + " " + mode + " Complete")
                input("Press any key to exit >>>")
        if mode == "interface":
            complete = new_interface(class_name, path_new)
            if complete:
                print(class_name + " " + mode + " Complete")
                input("Press any key to exit >>>")
        if mode == "abs":
            complete = new_abstract(class_name, path_new)
            if complete:
                print(class_name + " " + mode + " Complete")
                input("Press any key to exit >>>")
