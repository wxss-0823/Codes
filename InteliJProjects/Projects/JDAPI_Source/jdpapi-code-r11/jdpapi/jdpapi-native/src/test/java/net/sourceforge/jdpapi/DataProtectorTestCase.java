package net.sourceforge.jdpapi;

import java.io.File;

import junit.framework.TestCase;


public class DataProtectorTestCase extends TestCase {
    
    static {
        System.load(new File("target/jdpapi-native.dll").getAbsolutePath());;
    }
    
    public void testProtect() {
        DataProtector p = new DataProtector();
        
        byte [] data = p.protect("my key");
        
        assertEquals("my key", p.unprotect(data));
    }
    
    public void testProtectWithEntropy() {
        DataProtector p = new DataProtector("xxx".getBytes());
        DataProtector p2 = new DataProtector("xxx".getBytes());
        
        byte [] data = p.protect("my key");
        
        assertEquals("my key", p2.unprotect(data));
        
        p = new DataProtector("abc".getBytes());
        p2 = new DataProtector("def".getBytes());
        
        data = p.protect("my key");
        
        try {
            String result = p2.unprotect(data);
            fail("Instead of exception, received: " + result);
        } catch (DPAPIException expected) {
            
        }
    }
}
