using system;

public class isUnique{

    static bool uniqueString(String str)
    {
         
        for (int i = 0; i < str.Length; i++)
            for (int j = i + 1; j < str.Length; j++)
                if (str[i] == str[j])
                    return false;
 
        return true;
    }

    public static void Main()
    {
        string input = "apples"

        if (uniqueCharacters(input)){
            Console.WriteLine("The String " + input + " has all unique characters");
        } else {
            Console.WriteLine("The String " + input + " has duplicate characters");
        }   


    }

}