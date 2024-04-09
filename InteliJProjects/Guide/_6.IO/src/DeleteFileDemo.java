import java.io.File;

public class DeleteFileDemo {
    public static void deleteFolder(File folder) {
        File[] files = folder.listFiles();
        if (files != null) {
            for (File f : files) {
                if (f.isDirectory()) {
                    deleteFolder(f);
                } else {
                    f.delete();
                }
            }
        }
        folder.delete();
    }
    public static void main(String[] args) {
        // 这里修改为自己的测试目录
        File folder = new File("./_6.IO/tmp");
        deleteFolder(folder);
    }
}
