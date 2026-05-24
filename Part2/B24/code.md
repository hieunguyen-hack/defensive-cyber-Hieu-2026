import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class Document{
    public static void main(String[] args) {
        SecureDocument object = new SecureDocument("DOC-2026", "Classification: Top Secret - Database Access Granted!");
        object.permission("Alice", SecureDocument.AccessLevel.READ);
        object.permission("Auditor", SecureDocument.AccessLevel.READ);
        System.out.println("\n=== RUNNING ACCESS CONTROL EVALUATION ===");
        //test
        try {
            String data = object.readcontent("Alice", "guest");
            System.out.println("Alice Access Check: [SUCCESS] -> " + data);
        } catch (SecurityException e) {
            System.out.println("Alice Access Check: [FAILED] -> " + e.getMessage());
        }

        try{
            String data = object.readcontent("BOb", "Auditor");
            System.out.println("Bob Access Check: [SUCCESS] ->" + data);
        } catch(SecurityException e){
            System.out.println("Bob Access Check: [FAILED] -> " + e.getMessage());
        }

        try{
            String data = object.readcontent("hacker", "hacker");
            System.out.println("Hacker Access Check: [SUCCESS] ->" + data);
        } catch(SecurityException e){
            System.out.println("Hacker Access Check: [FAILED] -> " + e.getMessage());
        }
        
    }
}
//list of identiy and role, checking that list, if yes, print out document granted
// we need ID for identity of each documet
class SecureDocument{
    public enum AccessLevel{
        READ, WRITE, NONE
    }

    public final String documentID;
    public final String content;
    private final Map<String, AccessLevel>accessControlList = new ConcurrentHashMap<>();
    //list which stores each person's permission

    //constructor
    public SecureDocument(String documentID, String content){
        this.documentID = documentID;
        this.content = content;
    }
    //grant the permission for each person
    public void permission(String identity, AccessLevel level){
        if(identity != null && level != null){
            accessControlList.put(identity, level);
        }
    }

    //check if the person has the permission to read or write the file
    public boolean check(String user, String role){ //one is not the name in the system but has the role
        if(accessControlList.getOrDefault(user, AccessLevel.NONE) == AccessLevel.READ){
            return true;
        }
        if(accessControlList.getOrDefault(role, AccessLevel.NONE) == AccessLevel.READ){
            return true;
        }
        return false;
    }

    //read the content of the file if the check is true
    public String readcontent(String user, String role){
        if (check(user, role) == true){
            return this.content;
        }
        throw new SecurityException("403 Unauthorized: Denied access to document ID " + documentID);
    }
}   
